(ns examples.lifecycle-and-factory-demo
  "Demonstrates Component Lifecycle, Factory Method, and Adapter patterns.")

;; Lifecycle Protocol & Component
(defprotocol Lifecycle
  "Stuart Sierra Component lifecycle contract."
  (start [component])
  (stop [component]))

(defrecord DatabaseService [connection-string pool-size connection]
  Lifecycle
  (start [this]
    (println "Starting database connection pool...")
    (assoc this :connection {:status :connected}))
  (stop [this]
    (println "Stopping database connection pool...")
    (assoc this :connection nil)))

;; Factory Method helpers
(defn make-database-service
  "Factory helper creating configured DatabaseService with defaults."
  [conn-str]
  (map->DatabaseService {:connection-string conn-str
                         :pool-size 10
                         :connection nil}))

;; Adapter Pattern via extend-type
(defprotocol JsonSerializable
  "Target protocol for converting objects to JSON string."
  (to-json [this]))

(extend-type java.lang.String
  JsonSerializable
  (to-json [this]
    (str "\"" this "\"")))

(extend-type clojure.lang.PersistentHashMap
  JsonSerializable
  (to-json [this]
    (str "{" this "}")))
