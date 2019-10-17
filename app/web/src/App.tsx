import React from 'react';
import './App.css';
import Autosuggest from 'react-autosuggest';

interface Language {
  name: string,
  year: number
}

interface State {
  value: string,
  suggestions: Array<Language>
}

const languages : Array<Language> = [
  {
    name: 'C',
    year: 1972
  },
  {
    name: 'Elm',
    year: 2012
  }
];

// Teach Autosuggest how to calculate suggestions for any given input value.
const getSuggestions = (value: string) => {
  const inputValue = value.trim().toLowerCase();
  const inputLength = inputValue.length;

  return inputLength === 0 ? [] : languages.filter(lang =>
      lang.name.toLowerCase().slice(0, inputLength) === inputValue
  );
};

// When suggestion is clicked, Autosuggest needs to populate the input
// based on the clicked suggestion. Teach Autosuggest how to calculate the
// input value for every given suggestion.
const getSuggestionValue = (suggestion : Language) => suggestion.name;

// Use your imagination to render suggestions.
const renderSuggestion = (suggestion : Language) => (
    <div>
      {suggestion.name}
    </div>
);

class App extends React.Component<{}, State> {

  state = {
    value: '',
    suggestions: []
  };

  onChange = (event: Event, { newValue } : {newValue: string}) => {
    this.setState({
      value: newValue
    });
  };

  // Autosuggest will call this function every time you need to update suggestions.
  // You already implemented this logic above, so just use it.
  onSuggestionsFetchRequested = ({ value } : {value: string} ) => {
    this.setState({
      suggestions: getSuggestions(value)
    });
  };

  // Autosuggest will call this function every time you need to clear suggestions.
  onSuggestionsClearRequested = () => {
    this.setState({
      suggestions: []
    });
  };

  render() {
    const { value, suggestions } = this.state;

    // Autosuggest will pass through all these props to the input.
    const inputProps : any = {
      placeholder: 'Type any sentence',
      value,
      onChange: this.onChange
    };

    // Finally, render it!
    return (
        <div className="App">
          <header className="App-header">
            <p>
              Welcome to Word Prediction App!
            </p>
            <Autosuggest
                suggestions={suggestions}
                onSuggestionsFetchRequested={this.onSuggestionsFetchRequested}
                onSuggestionsClearRequested={this.onSuggestionsClearRequested}
                getSuggestionValue={getSuggestionValue}
                renderSuggestion={renderSuggestion}
                inputProps={inputProps}
            />
          </header>
        </div>
    );
  }
}

export default App;
