class AddIsReviewedToCitum < ActiveRecord::Migration[5.2]
  def change
    add_column :cita, :is_reviewed, :boolean
  end
end
