class CreateProducts < ActiveRecord::Migration[7.0]
  def change
    create_table :products do |t|
      t.integer :price
      t.string :category
      t.integer :amount
      t.string :name

      t.timestamps
    end
  end
end
