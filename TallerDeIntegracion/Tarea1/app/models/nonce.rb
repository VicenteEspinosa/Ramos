class Nonce < ApplicationRecord
end

# == Schema Information
#
# Table name: nonces
#
#  id         :bigint           not null, primary key
#  expiration :integer
#  scopes     :text             is an Array
#  value      :string
#  created_at :datetime         not null
#  updated_at :datetime         not null
#  user_id    :string
#
