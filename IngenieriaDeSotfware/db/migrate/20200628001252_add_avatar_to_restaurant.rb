class AddAvatarToRestaurant < ActiveRecord::Migration[5.2]
  def change
    add_column :restaurants, :avatar, :string
  end
end
