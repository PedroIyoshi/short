require 'bigdecimal'

repeticoes = 1000
BigDecimal.limit(10000)
resultado = BigDecimal(0)

for i in 0..repeticoes do
  resultado += BigDecimal(
    (1/BigDecimal(16**i)) *
    (
      (4/BigDecimal((8)*i + 1)) - 
      (2/BigDecimal((8)*i + 4)) - 
      (1/BigDecimal((8)*i + 5)) -
      (1/BigDecimal((8)*i + 6)) 
    )
  )
end

puts resultado