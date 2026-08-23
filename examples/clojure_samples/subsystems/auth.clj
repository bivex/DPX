(ns pattern-demo.subsystems.auth)

(defn verify-customer-session [customer-id]
  {:auth-token (str "tok-" customer-id) :valid? true})
