(ns pattern-demo.pipeline
  "Demonstration of Chain of Responsibility / Processing Pipeline pattern in Clojure.")

(defn wrap-rate-limiter
  "Middleware stage 1: Rate limiting."
  [handler max-requests]
  (fn [request]
    (if (> (:request-count request 0) max-requests)
      {:status 429 :body "Rate limit exceeded"}
      (handler (assoc request :rate-limited false)))))

(defn wrap-jwt-auth
  "Middleware stage 2: JWT Authentication."
  [handler]
  (fn [request]
    (if-let [token (get-in request [:headers "authorization"])]
      (handler (assoc request :user {:id "u-123" :token token}))
      {:status 401 :body "Unauthorized"})))

(defn wrap-cors-headers
  "Middleware stage 3: Cross-Origin Resource Sharing."
  [handler allowed-origin]
  (fn [request]
    (let [response (handler request)]
      (assoc-in response [:headers "Access-Control-Allow-Origin"] allowed-origin))))

(defn build-api-gateway-pipeline
  "Chain of Responsibility: composes request processing stages into a single sequential pipeline."
  [base-handler]
  (-> base-handler
      (wrap-rate-limiter 100)
      wrap-jwt-auth
      (wrap-cors-headers "*")))
