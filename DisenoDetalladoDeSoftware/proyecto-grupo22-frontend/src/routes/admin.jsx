import React, { Component } from 'react';
import { CardGrid } from '../components/cardGrid/cardGrid.component';
import { NavBar } from '../components/navbar/navbar.component';
import { SearchBox } from '../components/searchBox/searchBox.component';
import CategoryCreate from '../components/categoryCreate/categoryCreate.component';
import CategoryList from '../components/categoryList/categoryList.component';
import './admin.css';

class Admin extends Component {
    constructor() {
        super();
    
        this.state = {
          items: [],
          searchField: ''
        };
    }
    
    componentDidMount() {
        fetch(`${process.env.REACT_APP_BACKEND_URL}/products`)
            .then(response => response.json())
            .then(products => this.setState({ items: products.data }));
    }
    
    onSearchChange = event => {
        this.setState({ searchField: event.target.value });
    };
    
    render() {
        const { items, searchField } = this.state;
        const filteredItems = items.filter(item =>
            item.attributes.name.toLowerCase().includes(searchField.toLowerCase()) +
            item.attributes.brand.toLowerCase().includes(searchField.toLowerCase()) +
            item.attributes.category.toLowerCase().includes(searchField.toLowerCase())
        );

        return (
            <div className='Admin'>
                <NavBar route='Admin' />
                <div className='container'>
                    <div className='category-column'>
                        <CategoryCreate />
                        <CategoryList />
                    </div>
                    <div className='items-column'>
                        <SearchBox onSearchChange={this.onSearchChange} />
                        <CardGrid items={filteredItems} route='Admin' />
                        <div className='buttons'>
                            <button className='save-btn' type='button'>Guardar Cambios</button>
                            <button className='reset-btn' type='button'>Reiniciar Cambios</button>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default Admin;
