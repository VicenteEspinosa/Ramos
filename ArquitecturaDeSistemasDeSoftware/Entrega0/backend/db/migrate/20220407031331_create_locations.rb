class CreateLocations < ActiveRecord::Migration[7.0]
  def change
    create_table :locations do |t|
      t.float :lat
      t.float :long
      t.string :name
      t.references :user, null: false, foreign_key: true

      t.timestamps
    end
  end
end
