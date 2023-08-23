import { Container } from 'react-bootstrap'
import { Routes, Route, BrowserRouter } from 'react-router-dom'
import Header from './components/Header'
import Footer from './components/Footer'
import HomeScreen from './screens/HomeScreen'
import ProductScreen from './screens/ProductScreen'

function App() {
    return (
        <BrowserRouter>
            <Header />
            <main className="py-3">
                <Container>
                    <Routes>
                        <Route path='/' element={<HomeScreen />} exact></Route>
                        <Route path='/product/:id' element={<ProductScreen />} exact></Route>
                    </Routes>
                </Container>
            </main>
            <Footer />
        </BrowserRouter>
    );
}

export default App;
