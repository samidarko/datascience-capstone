import React from 'react';
import './App.css';
import {DebounceInput} from 'react-debounce-input';
// import {init, last, tail} from 'ramda'
import axios from 'axios'

class App extends React.Component {
    state = {
        value: '',
        predictions: []
    };

    onChange = event => {
        this.predict(event.target.value)
    };

    predict = value => {
        const values = value.split(' ');
        const data = {words: values};
        axios.post('http://127.0.0.1:5000/ ', data)
            .then(response => {
                this.setState({predictions: response.data})
            })
            .catch(function (error) {
                console.error(error);
            });
    };

    onClick = event => {
        const value = `${this.state.value ? `${this.state.value} ` : ''}${event.target.value}`;
        this.setState({value, predictions: []});
        this.predict(value + ' ')
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

                    <p>
                        {
                            this.state.predictions.map(
                                (prediction, i) => <button value={prediction} onClick={this.onClick} key={i}>{prediction}</button>)
                        }
                    </p>
                </header>
            </div>
        );
    }
}

export default App;
