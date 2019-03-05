def numeric
  cpf_root = Array.new(9) { rand(10) }

  # calculate first digit
  sum = (0..8).inject(0) do |sum, i|
    sum + cpf_root[i] * (10 - i)
  end

  first_validator = sum % 11
  first_validator = first_validator < 2 ? 0 : 11 - first_validator
  cpf_root << first_validator

  # calculate second digit
  sum = (0..8).inject(0) do |sum, i|
    sum + cpf_root[i] * (11 - i)
  end

  sum += first_validator * 2

  second_validator = sum % 11
  second_validator = second_validator < 2 ? 0 : 11 - second_validator
  (cpf_root << second_validator).to_s
end