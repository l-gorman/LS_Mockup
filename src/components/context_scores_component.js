import React from 'react';
import "./context_cards_style.css"


class FormInput extends React.Component {

    render() {
        return (
            <div className="form-group">
                <label htmlFor="Test Number" className="col-form-label"></label>
                <div>
                    <input onChange={(event) => this.props.onChange(event, { typology: this.props.typology, farmerexpert: this.props.farmerexpert, category: this.props.category })} type="number" min="0" max="4"></input>
                </div>
            </div >
        );
    }
}

const FormCategory = (props) => {
    // Ensuring that the label only prints on one side of the container
    let category_print = "";
    if (props.farmerexpert === "Farmer") {
        category_print = props.category;
    } else {
        category_print = "";
    }

    return (
        <div className="container">

            <p>{category_print} <br /> </p>
            <FormInput onChange={props.onChange} category={props.category} typology={props.typology} farmerexpert={props.farmerexpert} args={props.args} />

        </div >
    );
}

const FarmerExpertCard = (props) => {
    return (
        <div className="col farmer_expert_container">
            <h5 className="text-center">{props.farmerexpert}</h5>
            {props.args.categories.map((category) => (
                <FormCategory onChange={props.onChange} category={category} typology={props.typology} farmerexpert={props.farmerexpert} args={props.args} />
            ))}
        </div>
    );
}

const TypologyCard = (props) => {
    return (
        <div className="typology_card">
            <div key={props.typology} className="card">
                <h3 className="card-header text-center bg-dark text-white">Typology - {props.typology}</h3>
                <div className="row">
                    {props.args.farmerexpert.map((farmerexpert) => (
                        <FarmerExpertCard onChange={props.onChange} typology={props.typology} farmerexpert={farmerexpert} args={props.args} />
                    ))}
                </div>
            </div>
        </div>
    );
}
const SummaryCard = (props) => {
    return (
        <div className="typology_card">
            <div className="card">
                <h3 className="card-header text-center bg-dark text-white">Results</h3>
                <div>
                    Here is where I will put the results
                </div>
            </div>
        </div>
    );
}



// This is the main function that renders each of the context cards
class ContextCards extends React.Component {
    constructor(props) {
        super(props)

        this.args = {
            typologies: ["Low", "Medium", "High"],
            farmerexpert: ["Farmer", "Expert"],
            categories: ["Land", "Labour", "Seed", "Inputs and Services", "Knowledge and Skills", "Water", "Markets"],
            maximum_score: 4
        }


        // Initialising the state for all of the form inputs below
        this.state = []
        let i = 0;
        for (i = 0; i < this.args.typologies.length; i++) {
            let j = 0;
            for (j = 0; j < this.args.farmerexpert.length; j++) {
                let k = 0;
                for (k = 0; k < this.args.categories.length; k++) {
                    this.state.push({
                        value: 0,
                        typology: this.args.typologies[i],
                        farmerexpert: this.args.farmerexpert[j],
                        category: this.args.categories[k],
                    })
                }
            }
        }
    }

    onChange = (event, inputvalue) => {
        let newstate = this.state;
        if (event.target.value > 4) {
            alert("Please enter a score of 4 or less")
        }
        let i = 0;
        for (i = 0; i < newstate.length; i++) {
            if (newstate[i].typology === inputvalue.typology) {
                if (newstate[i].farmerexpert === inputvalue.farmerexpert) {
                    if (newstate[i].category === inputvalue.category) {
                        newstate[i].value = event.target.value // Do not fully understand how this sets the original state to what it needs to be :(
                    }
                }
            }
        }
        console.log(this.state);
    }




    render() {
        return (
            <div className="row  justify-content-center">
                {this.args.typologies.map((typology) => (
                    <TypologyCard typology={typology} args={this.args} onChange={this.onChange} />
                ))}
                <SummaryCard />
            </div>
        );
    }

}
export default ContextCards;


