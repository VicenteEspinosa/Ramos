class MakeUserColumnsNotNull < ActiveRecord::Migration[7.0]
  def change
    change_column_null :users, :username, false
    change_column_null :users, :name, false
    change_column_null :users, :age, false
    change_column_null :users, :psu_score, false
    change_column_null :users, :university, false
    change_column_null :users, :gpa_score, false
    change_column_null :users, :job, false
    change_column_null :users, :salary, false
    change_column_null :users, :promotion, false
    change_column_null :users, :hospital, false
    change_column_null :users, :medical_debt, false
  end
end
