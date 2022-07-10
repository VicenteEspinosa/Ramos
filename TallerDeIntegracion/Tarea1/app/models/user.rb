# == Schema Information
#
# Table name: users
#
#  id           :bigint           not null, primary key
#  age          :integer          not null
#  gpa_score    :float
#  hospital     :string
#  job          :string
#  medical_debt :float
#  name         :string           not null
#  operations   :text             default([]), is an Array
#  password     :string
#  promotion    :boolean          default(FALSE), not null
#  psu_score    :integer
#  salary       :float
#  university   :string
#  username     :string           not null
#  created_at   :datetime         not null
#  updated_at   :datetime         not null
#
class User < ApplicationRecord
end
