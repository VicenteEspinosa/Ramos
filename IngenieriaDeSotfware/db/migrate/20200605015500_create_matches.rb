class CreateMatches < ActiveRecord::Migration[5.2]
  def change
    create_table :matches do |t|
      t.integer :user_id
      t.references :user, foreign_key: true
      t.integer :user_2_id
      t.boolean :is_match

      t.timestamps
    end
  end
end
