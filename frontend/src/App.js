import React from 'react'
import axios from 'axios'
import logo from './logo.svg';
import './App.css';
import UserList from './components/users.js'
import TodoList from './components/todos.js'
import ProjectList from './components/projects.js'
import ProjectTodosList from './components/projecttodos.js'
import LoginForm from './components/LoginForm.js'
import MenuList from './components/menu.js'
import Footer from './components/footer.js'
import {HashRouter, BrowserRouter, Route, Link, Switch, Redirect } from 'react-router-dom'
import Cookies from 'universal-cookie'


const Page404 = ({location}) => {
    return <div>
        Page {location.pathname} not found.
    </div>
}

class App extends React.Component {
    constructor(props) {
            super(props)
            this.state = {
                'users': [],
                'projects': [],
                'todos': [],
                'token': '',
            }
    }

  set_token(token) {
    const cookies = new Cookies()
    cookies.set('token', token)
    this.setState({'token': token})
  }

  is_authenticated() {
    return this.state.token != ''
  }

  logout() {
    this.set_token('')
  }

  get_token_from_storage() {
    const cookies = new Cookies()
    const token = cookies.get('token')
    this.setState({'token': token})
  }

  get_token(login, password) {
    axios.post('http://127.0.0.1:8000/api-token-auth/', {username: login, password: password})
    .then(response => {
        this.set_token(response.data['token'])
    }).catch(error => alert('Неверный логин или пароль'))
  }

  load_data() {
        axios.get('http://127.0.0.1:8000/api/users/')
        .then(
            response => {
                const users = response.data
                this.setState({
                    'users': users
                })
            }
        ).catch(
            error =>  console.log(error)
        )

        axios.get('http://127.0.0.1:8000/api/projects/')
        .then(
            response => {
                const projects = response.data.results
                this.setState({
                    'projects': projects
                })
            }
        ).catch(
            error =>  console.log(error)
        )

        axios.get('http://127.0.0.1:8000/api/todos/')
        .then(
            response => {
                const todos = response.data.results

                this.setState({
                    'todos': todos
                })
            }
        ).catch(
            error =>  console.log(error)
        )
    }

  componentDidMount() {
    this.get_token_from_storage()
    this.load_data()
  }

    render() {
        return (
        <div>
            <HashRouter>
            <nav>
                <ul>
                    <li>
                        <Link to='/'>Users</Link>
                    </li>
                    <li>
                        <Link to='/todos'>Todos</Link>
                    </li>
                    <li>
                        <Link to='/projects'>Projects</Link>
                    </li>
                    <li>
                        {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                    </li>
                </ul>
            </nav>

            <Switch>
                <Route exact path='/' component={() => <UserList users={this.state.users} />} />
                <Route exact path='/todos' component={() => <TodoList todos={this.state.todos} />} />
                <Route exact path='/login' component={() => <LoginForm get_token={(login, password) => this.get_token(login, password)} />} />
                <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />} />
                <Route path='/project/:id'>
                    <ProjectTodosList todos={this.state.todos} />
                </Route>
                <Redirect from='/users' to ='/' />
                <Route component={Page404} />
            </Switch>
            </HashRouter>
            <Footer />
        </div>
        )
    }
}

export default App;
