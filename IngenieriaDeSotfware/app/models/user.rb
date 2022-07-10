class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable, :trackable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable
  has_and_belongs_to_many :gustos, :dependent => :delete_all
  belongs_to :city
  has_many :restaurants, :dependent => :delete_all
  has_many :comments, :dependent => :delete_all
  has_many :my_matches, :class_name => 'Match', foreign_key: 'user_id', :dependent => :delete_all
  has_many :foreign_matches, :class_name => 'Match', foreign_key: 'user_2_id', :dependent => :delete_all

  # attr_accessible :remove_avatar
  has_many :my_citum, :class_name => 'Cita', foreign_key: 'user_id', :dependent => :delete_all
  has_many :foreign_citum, :class_name => 'Cita', foreign_key: 'user_2_id', :dependent => :delete_all
  mount_uploader :avatar, AvatarUploader
end
