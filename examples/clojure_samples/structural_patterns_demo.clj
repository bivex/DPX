(ns pattern-demo.structural.api
  "Demonstration of Facade, Proxy (Virtual & Native), and Flyweight (Memoization) patterns."
  (:require [pattern-demo.subsystems.auth :as auth]
            [pattern-demo.subsystems.billing :as billing]
            [pattern-demo.subsystems.inventory :as inventory]))

;; ============================================================================
;; 1. FACADE PATTERN (Unified Subsystem Gateway)
;; ============================================================================

(defn checkout-customer-cart
  "Facade entrypoint: coordinates authentication, inventory reservation, and billing."
  [customer-id item-ids credit-card-token]
  (let [auth-token (auth/verify-customer-session customer-id)
        stock-ok?  (inventory/reserve-items item-ids)
        receipt    (billing/charge-card credit-card-token 250)]
    {:success true
     :order-id (str "ORD-" (System/currentTimeMillis))
     :auth auth-token
     :receipt receipt}))

(defn cancel-customer-order
  "Facade entrypoint: rolls back inventory and issues payment refund."
  [order-id charge-id item-ids]
  (inventory/release-items item-ids)
  (billing/refund-charge charge-id)
  {:status :cancelled :order order-id})


;; ============================================================================
;; 2. PROXY PATTERN (Lazy Virtual Proxy & Host Interop Proxy)
;; ============================================================================

(defonce lazy-heavy-database-pool
  "Virtual Proxy: delays costly connection pooling until first deref (@)."
  (delay
    (println "Initializing heavy physical database connections...")
    {:pool-id "pool-99" :active-connections 10}))

(defn create-async-runnable-proxy
  "Native Proxy: instantiates a Java Runnable surrogate wrapping a Clojure function."
  [task-fn]
  (proxy [java.lang.Runnable] []
    (run []
      (task-fn))))


;; ============================================================================
;; 3. FLYWEIGHT PATTERN (Shared Object Cache & Memoization)
;; ============================================================================

(defn- compute-complex-glyph-metrics [font-name char-code font-size]
  ;; Expensive mathematical glyph calculation
  {:glyph char-code :width (* font-size 0.6) :height font-size :kerning 0.05})

(def get-cached-glyph-metric
  "Flyweight pattern: caches fine-grained immutable glyph objects using memoize."
  (memoize compute-complex-glyph-metrics))
