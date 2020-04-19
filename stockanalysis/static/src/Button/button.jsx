import React, { Component } from 'react';
import PropTypes from 'prop-types';


const Anchor = (props) => <a {...props} />;
const _Button = (props) => <button {...props} />;


class Button extends Component {
    constructor(props) {
        this.checkProps(props);
    }

    checkProps(newProps) {
        const { element, href } = newProps;
        this.renderComponent = element || href ? Anchor: _Button;
    }

    render() {
        const ClassComponent = this.renderComponent;
        const { className, title } = this.props;
        return (
            <ClassComponent
                className={className}
                role="button"
                title={title}
            >
                <span>
                    
                </span>
            </ClassComponent>
        )
    }
}


Button.propTypes = {
    className: PropTypes.string,
    element: PropTypes.func,
    href: PropTypes.string,
    onPress: PropTypes.func,
    title: PropTypes.string.isRequired,
}


export default Button;