require 'rails_helper'

# rubocop:disable Metrics/BlockLength
describe 'Decison table movie form', type: :feature do
  before :each do
    avatar = Movie.create(title: 'Avatar')
    titanic = Movie.create(title: 'Titanic')
    toy_story = Movie.create(title: 'Toy Story')
    star_wars = Movie.create(title: 'Star Wars')

    cars = Movie.create(title: 'Cars')
    star_trek = Movie.create(title: 'Star Trek')
    spiderman = Movie.create(title: 'Spiderman')
    avengers = Movie.create(title: 'Avengers')

    MovieTime.create!(movie_id: avatar.id, rating: 'TODO ESPECTADOR', branch: 'Santiago',
                      language: 'Español', room: 1, time: 'MATINÉ',
                      date_start: Date.new(2023, 1, 1), date_end: Date.new(2023, 1, 2))
    MovieTime.create!(movie_id: titanic.id, rating: 'MAYORES DE 18 AÑOS', branch: 'Santiago',
                      language: 'Español', room: 2, time: 'TANDA', date_start: Date.new(2023, 1, 1),
                      date_end: Date.new(2023, 1, 2))
    MovieTime.create!(movie_id: toy_story.id, rating: 'TODO ESPECTADOR', branch: 'Regional',
                      language: 'Español', room: 3, time: 'NOCHE', date_start: Date.new(2023, 1, 1),
                      date_end: Date.new(2023, 1, 2))
    MovieTime.create!(movie_id: star_wars.id, rating: 'MAYORES DE 18 AÑOS', branch: 'Regional',
                      language: 'Español', room: 4, time: 'NOCHE', date_start: Date.new(2023, 1, 1),
                      date_end: Date.new(2023, 1, 2))

    MovieTime.create!(movie_id: cars.id, rating: 'TODO ESPECTADOR', branch: 'Santiago',
                      language: 'Ingles', room: 5, time: 'TANDA', date_start: Date.new(2023, 1, 1),
                      date_end: Date.new(2023, 1, 2))
    MovieTime.create!(movie_id: star_trek.id, rating: 'MAYORES DE 18 AÑOS', branch: 'Santiago',
                      language: 'Ingles', room: 6, time: 'NOCHE', date_start: Date.new(2023, 1, 1),
                      date_end: Date.new(2023, 1, 2))
    MovieTime.create!(movie_id: spiderman.id, rating: 'TODO ESPECTADOR', branch: 'Regional',
                      language: 'Ingles', room: 7, time: 'TANDA', date_start: Date.new(2023, 1, 1),
                      date_end: Date.new(2023, 1, 2))
    MovieTime.create!(movie_id: avengers.id, rating: 'MAYORES DE 18 AÑOS', branch: 'Regional',
                      language: 'Ingles', room: 8, time: 'MATINÉ', date_start: Date.new(2023, 1, 1),
                      date_end: Date.new(2023, 1, 2))
  end

  scenario 'Case 1' do
    visit '/'
    fill_in 'date', with: Date.new(2023, 1, 1)
    select 'TODO ESPECTADOR', from: 'rating'
    select 'Santiago', from: 'branch'
    select 'Español', from: 'language'
    click_button 'Buscar'
    expect(page).to have_content('Avatar') and expect(page).to have_content('Cars') and
      expect(page).not_to have_content('Toy Story') and expect(page).not_to have_content('Titanic')
  end

  scenario 'Case 2' do
    visit '/'
    fill_in 'date', with: Date.new(2023, 1, 1)
    select 'MAYORES DE 18 AÑOS', from: 'rating'
    select 'Santiago', from: 'branch'
    select 'Español', from: 'language'
    click_button 'Buscar'
    expect(page).to have_content('Avatar') and expect(page).to have_content('Titanic') and
      expect(page).not_to have_content('Toy Story') and expect(page).not_to have_content('Avengers')
  end

  scenario 'Case 3' do
    visit '/'
    fill_in 'date', with: Date.new(2023, 1, 1)
    select 'TODO ESPECTADOR', from: 'rating'
    select 'Santiago', from: 'branch'
    select 'Ingles', from: 'language'
    click_button 'Buscar'
    expect(page).to have_content('Avatar') and expect(page).to have_content('Cars') and
      expect(page).not_to have_content('Toy Story') and expect(page).not_to have_content('Titanic')
  end

  scenario 'Case 4' do
    visit '/'
    fill_in 'date', with: Date.new(2023, 1, 1)
    select 'MAYORES DE 18 AÑOS', from: 'rating'
    select 'Santiago', from: 'branch'
    select 'Español', from: 'language'
    click_button 'Buscar'
    expect(page).to have_content('Avatar') and expect(page).to have_content('Titanic') and
      expect(page).not_to have_content('Toy Story') and
      expect(page).not_to have_content('Spiderman')
  end

  scenario 'Case 5' do
    visit '/'
    fill_in 'date', with: Date.new(2023, 1, 1)
    select 'TODO ESPECTADOR', from: 'rating'
    select 'Regional', from: 'branch'
    select 'Ingles', from: 'language'
    click_button 'Buscar'
    expect(page).to have_content('Spiderman') and expect(page).to have_content('Toy Story') and
      expect(page).not_to have_content('Avatar') and expect(page).not_to have_content('Avengers')
  end

  scenario 'Case 6' do
    visit '/'
    fill_in 'date', with: Date.new(2023, 1, 1)
    select 'MAYORES DE 18 AÑOS', from: 'rating'
    select 'Regional', from: 'branch'
    select 'Ingles', from: 'language'
    click_button 'Buscar'
    expect(page).to have_content('Spiderman') and expect(page).to have_content('Avengers') and
      expect(page).not_to have_content('Avatar') and expect(page).not_to have_content('Start Trek')
  end

  scenario 'Case 7' do
    visit '/'
    fill_in 'date', with: Date.new(2023, 1, 1)
    select 'MAYORES DE 18 AÑOS', from: 'rating'
    select 'Regional', from: 'branch'
    select 'Español', from: 'language'
    click_button 'Buscar'
    expect(page).to have_content('Spiderman') and expect(page).to have_content('Avengers') and
      expect(page).not_to have_content('Avatar') and expect(page).not_to have_content('Start Trek')
  end

  scenario 'Case 8' do
    visit '/'
    fill_in 'date', with: Date.new(2023, 1, 1)
    select 'TODO ESPECTADOR', from: 'rating'
    select 'Regional', from: 'branch'
    select 'Español', from: 'language'
    click_button 'Buscar'
    expect(page).to have_content('Spiderman') and expect(page).to have_content('Toy Story') and
      expect(page).not_to have_content('Avatar') and expect(page).not_to have_content('Avengers')
  end
end
# rubocop:enable Metrics/BlockLength
