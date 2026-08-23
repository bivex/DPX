(ns examples.observer-demo
  "Demonstrates Observer pattern in Clojure with watched atoms and callbacks.")

(defonce system-events (atom {:active-listeners 0 :last-event nil}))

(defn- on-system-event-changed
  "Observer callback satisfying [key ref old-state new-state] signature."
  [key ref old-state new-state]
  (println (str "State changed under key " key ": from " old-state " to " new-state)))

(defn init-event-observers!
  []
  (add-watch system-events :audit-logger on-system-event-changed))
