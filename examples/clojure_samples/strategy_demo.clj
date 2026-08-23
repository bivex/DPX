(ns examples.strategy-demo
  "Demonstrates Strategy pattern in Clojure via Multimethods and Protocols.")

;; Strategy via Multimethod polymorphic dispatch
(defmulti calculate-shipping-cost
  "Calculates shipping cost using distinct strategy implementations."
  (fn [order] (:delivery-tier order)))

(defmethod calculate-shipping-cost :standard
  [order]
  (* (:weight order) 1.5))

(defmethod calculate-shipping-cost :express
  [order]
  (+ 10.0 (* (:weight order) 3.0)))

(defmethod calculate-shipping-cost :overnight
  [order]
  (+ 25.0 (* (:weight order) 5.0)))


;; Strategy via Protocols & Records
(defprotocol CompressionAlgorithm
  "Strategy interface for data compression."
  (compress [this byte-data])
  (decompress [this compressed-data]))

(defrecord GzipStrategy [buffer-size]
  CompressionAlgorithm
  (compress [this byte-data]
    (byte-array (count byte-data)))
  (decompress [this compressed-data]
    (byte-array (count compressed-data))))

(defrecord SnappyStrategy [compression-level]
  CompressionAlgorithm
  (compress [this byte-data]
    (byte-array (count byte-data)))
  (decompress [this compressed-data]
    (byte-array (count compressed-data))))
