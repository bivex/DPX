(ns pattern-demo.subsystems.inventory)

(defn reserve-items [item-ids]
  {:reserved-count (count item-ids) :reserved? true})

(defn release-items [item-ids]
  {:released-count (count item-ids) :released? true})
