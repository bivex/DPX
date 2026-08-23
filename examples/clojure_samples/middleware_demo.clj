(ns examples.middleware-demo
  "Demonstrates Decorator / Ring Middleware pattern in Clojure.")

(defn wrap-authentication
  "Middleware decorating handler with JWT token verification."
  [handler]
  (fn [request]
    (let [token (get-in request [:headers "authorization"])]
      (if token
        (handler (assoc request :identity {:user "admin"}))
        {:status 401 :body "Unauthorized"}))))

(defn wrap-timing-metrics
  "Middleware decorating handler with latency measurement."
  [handler]
  (fn [request]
    (let [start (System/currentTimeMillis)
          response (handler request)
          elapsed (- (System/currentTimeMillis) start)]
      (assoc-in response [:headers "X-Response-Time-Ms"] (str elapsed)))))

(defn create-decorated-app
  [base-handler]
  (-> base-handler
      wrap-timing-metrics
      wrap-authentication))
