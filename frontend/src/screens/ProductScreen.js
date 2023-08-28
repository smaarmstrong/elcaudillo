import React from 'react'
import { Link, useParams } from 'react-router-dom'
import { Row, Col, Image, ListGroup, Button, Card } from 'react-bootstrap'
import Rating from '../components/Rating'
import products from '../products'

function ProductScreen({ match }) {
    const product_id = useParams()
    const product = products.find((p) => p._id === product_id.id)

    return (
        <div>
            <Link to='/' className='btn btn-light my-3'>Go Back</Link>
        </div>
    )
}

export default ProductScreen
