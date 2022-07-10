class NullableColumns < ActiveRecord::Migration[7.0]
  def change
    change_column_null :users, :psu_score, true
    change_column_null :users, :gpa_score, true
    change_column_null :users, :salary, true
    change_column_null :users, :medical_debt, true
    change_column_null :users, :university, true
    change_column_null :users, :job, true
    change_column_null :users, :hospital, true
  end
end