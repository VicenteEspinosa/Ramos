class DefaultValueParams < ActiveRecord::Migration[7.0]
  def change
    change_column_default :users, :psu_score, nil
    change_column_default :users, :gpa_score, nil
    change_column_default :users, :salary, nil
    change_column_default :users, :medical_debt, nil
    change_column_default :users, :university, nil
    change_column_default :users, :job, nil
    change_column_default :users, :hospital, nil
  end
end