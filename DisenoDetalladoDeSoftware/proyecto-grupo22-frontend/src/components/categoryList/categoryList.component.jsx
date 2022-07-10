import React, { Component } from 'react';
import { FaEdit, FaTrash } from 'react-icons/fa';
import './categoryList.styles.css';

class CategoryList extends Component {
    constructor() {
        super();

        this.state = { categories: [] };
        this.deleteCategory = this.deleteCategory.bind(this);
    }
    componentDidMount() {
        fetch(`${process.env.REACT_APP_BACKEND_URL}/categories`)
            .then(response => response.json())
            .then(data => this.setState({ categories: data.data }));
    }
    deleteCategory(e, id) {
        fetch(`${process.env.REACT_APP_BACKEND_URL}/categories/${id}`, {
            method: 'DELETE',
            headers: {'Content-Type':'application/json'},
            body: JSON.stringify({
             "id": id
            })
        });
        this.setState({
            categories: this.state.categories.filter((c) => c.id !== id)
        })
        e.preventDefault();
    }

    render() {
        const { categories } = this.state;

        return (
            <div>
                <p>Recarga la página para actualizar la tabla!</p>
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nombre</th>
                            <th>Editar</th>
                            <th>Eliminar</th>
                        </tr>
                    </thead>
                    <tbody>
                        {categories.map((category, id) => {
                            return (
                                <tr key={id}>
                                    <td>{category.id}</td>
                                    <td>{category.name}</td>
                                    <td><button><FaEdit /></button></td>
                                    <td><button onClick={(e) => this.deleteCategory(e, category.id)}><FaTrash /></button></td>
                                </tr>
                            )
                        })}
                    </tbody>
                </table>
            </div>
        )
    }
};

export default CategoryList;
