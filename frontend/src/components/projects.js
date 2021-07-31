import React from 'react'
import { Link } from 'react-router-dom'

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td><Link to={`project/${parseInt(project.id)}`}>{project.ProjectName}</Link></td>
            <td>{project.url}</td>

        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <th>
                id
            </th>
            <th>
                Project name
            </th>
            <th>
                url
            </th>

            {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectList