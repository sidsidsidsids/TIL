package mydict

import "errors"

// Dictionary type
type Dictionary map[string]string

var (
	errNotFound   = errors.New("Not Found")
	errWordExists = errors.New("That word already exists")
	errCantUpdate = errors.New("Non-existing Word")
)

// Search for a word
func (d Dictionary) Search(word string) (string, error) {
	value, exists := d[word]
	if exists {
		return value, nil
	}
	return "", errNotFound
}

// Add a word to the dictionary
func (d Dictionary) Add(word, def string) error {
	_, err := d.Search(word)
	switch err {
	case errNotFound:
		d[word] = def
	case nil:
		return errWordExists
	}
	return nil
}

// Update a word definition in dictionary
func (d Dictionary) Update(word, definition string) error {
	_, err := d.Search(word)
	switch err {
	case nil:
		d[word] = definition
	case errNotFound:
		return errCantUpdate
	}
	return nil
}

// Delete a word in dictionary
func (d Dictionary) Delete(word string) {
	delete(d, word)
}