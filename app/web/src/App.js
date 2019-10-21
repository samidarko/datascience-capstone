import React from 'react';
import './App.css';
import {DebounceInput} from 'react-debounce-input';
import {init, last, tail} from 'ramda'
import axios from 'axios'

class App extends React.Component {
    state = {
        value: '',
        predictions: []
    };

    onChange = event => {
        const values = event.target.value.split(' ');
        // const data = values.length > 1 ? {words: init(values), chars: last(values)} : {chars: last(values)};
        const data = {words: values};
        console.log(data)
        axios.post('http://127.0.0.1:5000/ ', data)
            .then(response => {
                this.setState({predictions: response.data})
            })
            .catch(function (error) {
                console.error(error);
            });
    };

    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <p>
                        Coursera Data-Science Specialization
                    </p>
                    <DebounceInput
                        placeholder={'type here'}
                        value={this.state.value}
                        minLength={2}
                        debounceTimeout={500}
                        onChange={this.onChange}/>

                    <ul>
                        {this.state.predictions.map(prediction => <li key={prediction}>{prediction}</li>)}
                    </ul>
                </header>
            </div>
        );
    }
}

export default App;
