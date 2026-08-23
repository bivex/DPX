(ns pattern-demo.creational
  "Demonstration of Builder and Abstract Factory patterns in Clojure.")

;; ============================================================================
;; 1. BUILDER PATTERN (Fluent Step-by-Step Configuration)
;; ============================================================================

(defn make-server-config-builder
  "Creates the initial builder accumulator for server configuration."
  []
  {:host "127.0.0.1" :port 8080 :ssl? false :max-threads 8})

(defn with-host
  "Builder step: configures hostname."
  [builder host]
  (assoc builder :host host))

(defn with-port
  "Builder step: configures port."
  [builder port]
  (assoc builder :port port))

(defn with-ssl-certificate
  "Builder step: enables SSL and assigns cert path."
  [builder cert-path]
  (assoc builder :ssl? true :cert-file cert-path))

(defn with-max-threads
  "Builder step: configures thread pool capacity."
  [builder thread-count]
  (assoc builder :max-threads thread-count))

(defn build-server-config
  "Terminal builder step: validates and finalizes configuration map."
  [builder]
  (when (< (:port builder) 1024)
    (println "Warning: Privileged port configured."))
  (assoc builder :built-at (System/currentTimeMillis) :frozen true))


;; ============================================================================
;; 2. ABSTRACT FACTORY PATTERN (Family of Related Product Creators)
;; ============================================================================

(defprotocol CloudInfrastructureFactory
  "Abstract Factory interface: defines creation methods for cloud service families."
  (create-blob-storage [this config] "Creates a blob/object storage client.")
  (create-message-queue [this config] "Creates a message queue client."))

(defrecord AwsInfrastructureFactory [region]
  CloudInfrastructureFactory
  (create-blob-storage [this config]
    {:provider :aws-s3 :bucket (:bucket config) :region region})
  (create-message-queue [this config]
    {:provider :aws-sqs :queue-name (:queue config) :region region}))

(defrecord GcpInfrastructureFactory [project-id]
  CloudInfrastructureFactory
  (create-blob-storage [this config]
    {:provider :gcp-gcs :bucket (:bucket config) :project project-id})
  (create-message-queue [this config]
    {:provider :gcp-pubsub :topic (:topic config) :project project-id}))
