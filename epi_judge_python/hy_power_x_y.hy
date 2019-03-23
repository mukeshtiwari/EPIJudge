
(defn power [x y]
  (cond 
   [(= y 0) 1.0]
   [(= y 1) x]
   [(even? y)
       (do
          (setv t (power x (// y 2)))
          (* t t))]
   [True 
       (do
          (setv t (power x (// y 2)))
          (* x t t))]))

(print (power 2 60))
