class CreateCities < ActiveRecord::Migration[5.2]
  def change
    create_table :cities do |t|
      t.integer :city_id
      t.string :name

      t.timestamps
    end
  end
end
