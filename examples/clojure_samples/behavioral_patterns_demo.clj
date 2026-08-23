(ns pattern-demo.behavioral
  "Demonstration of Template Method, Command/CQRS, and State Machine (FSM) patterns in idiomatic Clojure."
  (:require [clojure.string :as str]))

;; ============================================================================
;; 1. TEMPLATE METHOD PATTERN (Resource Bracket & Algorithmic Skeleton)
;; ============================================================================

(defmacro with-database-tx
  "Template Method bracket macro: encapsulates setup, try/catch/finally,
  and transaction lifecycle hooks around user code."
  [[tx-binding db-pool] & body]
  `(let [conn# (get-connection ~db-pool)
         ~tx-binding (start-transaction conn#)]
     (try
       (let [result# (do ~@body)]
         (commit-transaction ~tx-binding)
         result#)
       (catch Exception err#
         (rollback-transaction ~tx-binding)
         (throw err#))
       (finally
         (release-connection conn#)))))

(defn with-benchmark-timer
  "Template Method higher-order function executing an action with setup and teardown timing."
  [action-name action-fn]
  (let [start-nano (System/nanoTime)]
    (try
      (action-fn)
      (finally
        (let [elapsed (/ (- (System/nanoTime) start-nano) 1000000.0)]
          (println (str "Task '" action-name "' completed in " elapsed " ms")))))))


;; ============================================================================
;; 2. COMMAND / CQRS PATTERN (Message Dispatching & Decoupled Execution)
;; ============================================================================

(defmulti handle-bank-command
  "Command pattern: polymorphic dispatcher routing command messages by :type."
  (fn [command-msg] (:type command-msg)))

(defmethod handle-bank-command :deposit [cmd]
  (let [{:keys [account-id amount]} cmd]
    {:status :success :action :deposit :account account-id :credited amount}))

(defmethod handle-bank-command :withdraw [cmd]
  (let [{:keys [account-id amount]} cmd]
    (if (> amount 5000)
      {:status :failed :reason "Exceeds daily withdrawal limit"}
      {:status :success :action :withdraw :account account-id :debited amount})))

(defmethod handle-bank-command :transfer [cmd]
  (let [{:keys [from-acc to-acc amount]} cmd]
    {:status :success :action :transfer :from from-acc :to to-acc :transferred amount}))


;; ============================================================================
;; 3. STATE / FINITE STATE MACHINE (FSM) PATTERN
;; ============================================================================

(defmulti transition-order-state
  "State pattern: FSM state machine dispatching on composite [current-status event-type]."
  (fn [order-state event] [(:status order-state) (:type event)]))

(defmethod transition-order-state [:created :pay] [order event]
  (assoc order :status :paid :payment-ref (:payment-id event)))

(defmethod transition-order-state [:paid :ship] [order event]
  (assoc order :status :shipped :tracking-no (:tracking-code event)))

(defmethod transition-order-state [:shipped :deliver] [order _]
  (assoc order :status :delivered :delivered-at (System/currentTimeMillis)))

(defmethod transition-order-state [:created :cancel] [order event]
  (assoc order :status :cancelled :cancel-reason (:reason event)))
