(ns pattern-demo.subsystems.billing)

(defn charge-card [card-token amount]
  {:charge-id (str "ch-" (System/currentTimeMillis)) :amount amount :status :captured})

(defn refund-charge [charge-id]
  {:refund-id (str "ref-" charge-id) :status :refunded})
