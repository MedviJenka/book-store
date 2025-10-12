import { View, Text, StyleSheet } from 'react-native'


const BOOK_SERVICE_URL = "http://10.0.0.1:5000/api/v1"


const getBooks = async ()=> {
    const endpoint = `${BOOK_SERVICE_URL}/books`
    const response = await fetch(endpoint)
    return response.json()
}


const App =()=> {

    return(
        <View style={ styles.container }>
            <Text style={ styles.text }>
                {getBooks()}
            </Text>
        </View>
    )
}


export default App


const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center'
    },
    text: {
        color: 'white',
        fontWeight: 'bold'
    }
})