class Restaurant < ApplicationRecord
  belongs_to :city
  belongs_to :user
  has_many :citum
  geocoded_by :address
  after_validation :geocode

  def address
    city = City.find(city_id).name
    [location, city, 'Santiago', 'Chile'].compact.join(', ')
  end
  mount_uploader :avatar, AvatarUploader
end
