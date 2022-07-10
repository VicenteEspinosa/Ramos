class CreateProducts < ActiveRecord::Migration[7.0]
  def change
    create_table :products do |t|
      t.string :name
      t.integer :price
      t.string :brand
      t.references :category, null: false, foreign_key: true
      t.string :image

      t.timestamps
    end
  end
end
