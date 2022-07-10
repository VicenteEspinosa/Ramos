class CreateUsers < ActiveRecord::Migration[7.0]
  def change
    create_table :users do |t|
      t.string :username
      t.string :password
      t.string :name
      t.integer :age
      t.integer :psu_score
      t.string :university
      t.float :gpa_score
      t.string :job
      t.float :salary
      t.boolean :promotion
      t.string :hospital
      t.text :operations, array:true, default: []
      t.float :medical_debt

      t.timestamps
    end
  end
end
