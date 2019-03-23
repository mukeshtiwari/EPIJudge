
(defn gcd [x y]
   (if (= x 0)
       y
       (gcd (% y x) x)))


(print (gcd  424953311 11))
