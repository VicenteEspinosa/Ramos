class CreateCoupons < ActiveRecord::Migration[7.0]
  def change
    create_table :coupons do |t|
      t.string :name
      t.integer :value
      t.integer :category_id

      t.timestamps
    end
    add_index :coupons, :category_id
  end
end
