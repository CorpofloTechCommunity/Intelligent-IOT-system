import React from 'react'
import { Card, CardBody, CardHeader, Img } from 'reactstrap'

const Home = () => {
    return (
        <div>
            <div className="container">
                <div className="row">
                    <Card className="card">
                        <CardHeader className="text-center">
                            Inteligent IOT System
                        </CardHeader>
                        <CardBody>   
                            <img className="image-fuild" src="https://images.unsplash.com/photo-1556114846-f753bec8a9f5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60" max-height="400" max-width="auto" alt="silo image"/>
                        </CardBody>
                    </Card>
                </div>
            </div>
            
        </div>
    )
}

export default Home;
