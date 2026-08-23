(ns pattern-demo.gof-complete
  "Demonstration of Prototype, Composite, Bridge, Iterator, Mediator, Memento, Visitor, and Interpreter patterns."
  (:require [clojure.string :as str]
            [clojure.walk :as walk]))

;; ============================================================================
;; 1. PROTOTYPE PATTERN (Instance Cloning & Derivation)
;; ============================================================================

(defprotocol PrototypeCloneable
  "Prototype interface for cloning objects with overrides."
  (clone-instance [this overrides]))

(defrecord DocumentTemplate [header body footer watermark]
  PrototypeCloneable
  (clone-instance [this overrides]
    (map->DocumentTemplate (merge this overrides))))

(defn clone-task-definition
  "Prototype helper function deriving customized task definition from template."
  [proto-task override-map]
  (merge proto-task override-map {:derived-at (System/currentTimeMillis)}))


;; ============================================================================
;; 2. COMPOSITE PATTERN (Part-Whole Tree Hierarchy)
;; ============================================================================

(defprotocol RenderableComponent
  "Composite interface unifying Leaf and Composite elements."
  (render-html [this]))

(defrecord ButtonElement [label on-click]
  RenderableComponent
  (render-html [this]
    (str "<button onclick='" on-click "'>" label "</button>")))

(defrecord CardContainer [title children-components]
  RenderableComponent
  (render-html [this]
    (str "<div class='card'><h2>" title "</h2>"
         (str/join (map render-html children-components))
         "</div>")))


;; ============================================================================
;; 3. BRIDGE PATTERN (Decoupled Abstraction & Implementation Driver)
;; ============================================================================

(defprotocol StorageEngineDriver
  "Low-level backend driver interface."
  (write-bytes [this path data])
  (read-bytes [this path]))

(defrecord DocumentRepository [storage-driver base-path]
  "High-level abstraction delegating physical persistence to decoupled driver."
  (save-document [this filename content]
    (let [full-path (str base-path "/" filename)]
      (write-bytes storage-driver full-path (.getBytes (str content)))))
  (load-document [this filename]
    (read-bytes storage-driver (str base-path "/" filename))))


;; ============================================================================
;; 4. ITERATOR PATTERN (Lazy Sequence Element Traversal)
;; ============================================================================

(defn fibonacci-number-seq
  "Iterator pattern: generates infinite lazy stream of Fibonacci numbers."
  ([] (fibonacci-number-seq 0 1))
  ([a b]
   (lazy-seq
     (cons a (fibonacci-number-seq b (+ a b))))))


;; ============================================================================
;; 5. MEDIATOR PATTERN (Decoupled Event Bus Coordination)
;; ============================================================================

(defprotocol EventBrokerHub
  "Mediator interface: central hub for pub/sub decoupling."
  (publish-event [this topic payload])
  (subscribe-topic [this topic handler-fn]))

(defrecord CentralMessageHub [subscribers-atom]
  EventBrokerHub
  (publish-event [this topic payload]
    (doseq [handler (get @subscribers-atom topic)]
      (handler payload)))
  (subscribe-topic [this topic handler-fn]
    (swap! subscribers-atom update topic (fnil conj []) handler-fn)))


;; ============================================================================
;; 6. MEMENTO PATTERN (State Capture & Rollback)
;; ============================================================================

(defn save-state-snapshot
  "Memento creator: captures snapshot of editor state."
  [editor-state]
  {:snapshot-id (System/currentTimeMillis)
   :saved-content (:text editor-state)
   :caret-offset (:caret editor-state)})

(defn restore-state-snapshot
  "Memento restorer: rolls back state to previous snapshot."
  [saved-snapshot]
  {:text (:saved-content saved-snapshot)
   :caret (:caret-offset saved-snapshot)
   :restored true})


;; ============================================================================
;; 7. VISITOR PATTERN (Tree Traversal & Node Operations)
;; ============================================================================

(defmulti visit-expression-node
  "Visitor pattern: polymorphic tree traversal over AST nodes."
  (fn [ast-node visitor-ctx] (:tag ast-node)))

(defmethod visit-expression-node :binary-op [node ctx]
  (str "(" (visit-expression-node (:left node) ctx)
       " " (:operator node) " "
       (visit-expression-node (:right node) ctx) ")"))

(defmethod visit-expression-node :literal-val [node _]
  (str (:value node)))

(defn walk-and-optimize-ast
  "Visitor helper using clojure.walk."
  [ast-tree]
  (walk/postwalk
    (fn [form]
      (if (and (map? form) (= (:tag form) :noop))
        nil
        form))
    ast-tree))


;; ============================================================================
;; 8. INTERPRETER PATTERN (Domain Expression Evaluator)
;; ============================================================================

(defmulti evaluate-ast-expression
  "Interpreter pattern: interprets domain grammar expressions in given environment."
  (fn [expr env] (:op expr)))

(defmethod evaluate-ast-expression :add [expr env]
  (+ (evaluate-ast-expression (:left expr) env)
     (evaluate-ast-expression (:right expr) env)))

(defmethod evaluate-ast-expression :multiply [expr env]
  (* (evaluate-ast-expression (:left expr) env)
     (evaluate-ast-expression (:right expr) env)))

(defmethod evaluate-ast-expression :variable [expr env]
  (get env (:var-name expr) 0))

(defmethod evaluate-ast-expression :constant [expr _]
  (:value expr))
