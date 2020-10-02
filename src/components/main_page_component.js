import React from 'react';
import Form from './form_component';
import './main_page_style.css'




class MainPage extends React.Component {
    render() {
        return (
            <div>
                <div className="container rounded-bottom header center bg-secondary text-center text-white">
                    <h1>Welcome to the LegumeChoice Tool</h1>
                </div>

                <div className="container rounded center bg-secondary form">
                    <Form />


                </div>
            </div>
        );
    }
}

export default MainPage;