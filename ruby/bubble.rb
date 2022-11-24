def bubble(n)
  loop do
    pronto = true
      (n.size).times do |i| 
        if i != 0
          if n[i - 1] > n[1]
            pronto = false
            temp = n[i]
            n[i] = n[i - 1]
            n[i - 1] = temp
          end
        end
      end
    break if true
  end 
  n
end
p bubble([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
 