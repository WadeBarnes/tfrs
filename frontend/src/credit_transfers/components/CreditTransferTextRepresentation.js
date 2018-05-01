import React, { Component } from 'react';
import PropTypes from 'prop-types';
import moment from 'moment';
import numeral from 'numeral';

import * as NumberFormat from '../../constants/numeralFormats';
import { CREDIT_TRANSFER_STATUS, CREDIT_TRANSFER_TYPES } from '../../constants/values';

class CreditTransferTextRepresentation extends Component {
  constructor (props) {
    super(props);

    this.creditsFrom = this.props.creditsFrom.name;
    this.creditsTo = this.props.creditsTo.name;
    this.fairMarketValuePerCredit =
      numeral(this.props.fairMarketValuePerCredit).format(NumberFormat.CURRENCY);
    this.numberOfCredits = numeral(this.props.numberOfCredits).format(NumberFormat.INT);
    this.totalValue = numeral(this.props.totalValue).format(NumberFormat.CURRENCY);
    this.tradeEffectiveDate = (this.props.tradeEffectiveDate)
      ? moment(this.props.tradeEffectiveDate).format('LL') : 'approval';

    this.tradeStatus = (this.props.status.id === CREDIT_TRANSFER_STATUS.approved.id ||
      this.props.status.id === CREDIT_TRANSFER_STATUS.completed.id)
      ? CREDIT_TRANSFER_STATUS.approved.description : this.props.status.status;
  }

  _buyAction () {
    return (this.props.status.id === CREDIT_TRANSFER_STATUS.approved.id ||
      this.props.status.id === CREDIT_TRANSFER_STATUS.completed.id)
      ? ' bought '
      : ' is proposing to buy ';
  }

  _sellAction () {
    return (this.props.status.id === CREDIT_TRANSFER_STATUS.approved.id ||
      this.props.status.id === CREDIT_TRANSFER_STATUS.completed.id)
      ? ' sold '
      : ' is proposing to sell ';
  }

  render () {
    switch (this.props.tradeType.id) {
      case CREDIT_TRANSFER_TYPES.sell.id:
        return (
          <div className="text-representation">
            <span className="value">{this.creditsFrom}</span> {this._sellAction()}
            <span className="value"> {this.numberOfCredits} </span> credit{(this.numberOfCredits > 1) && 's'} to
            <span className="value"> {this.creditsTo} </span>
            for <span className="value"> {this.fairMarketValuePerCredit} </span> per credit
            for a total value of <span className="value"> {this.totalValue}</span>,
            effective <span className="value"> {this.tradeEffectiveDate}</span>.
          </div>
        );
      case CREDIT_TRANSFER_TYPES.buy.id:
        return (
          <div className="text-representation">
            <span className="value">{this.creditsTo}</span> {this._buyAction()}
            <span className="value"> {this.numberOfCredits} </span> credit{(this.numberOfCredits > 1) && 's'} from
            <span className="value"> {this.creditsFrom} </span>
            for <span className="value"> {this.totalValue} </span>
            effective on <span className="value"> {this.tradeEffectiveDate}</span>.
          </div>
        );
      case CREDIT_TRANSFER_TYPES.validation.id:
        return (
          <div className="text-representation">
            A <span className="value">validation</span> of
            <span className="value"> {this.numberOfCredits} </span>
            credit{(this.numberOfCredits > 1) && 's'} earned by
            <span className="value"> {this.creditsTo} </span>
            has been <span className="value lowercase"> {this.tradeStatus}</span>,
            effective on <span className="value"> {this.tradeEffectiveDate}</span>.
          </div>
        );
      case CREDIT_TRANSFER_TYPES.retirement.id:
        return (
          <div className="text-representation">
            A <span className="value">reduction</span> of
            <span className="value"> {this.numberOfCredits} </span>
            credit{(this.numberOfCredits > 1) && 's'} earned by
            <span className="value"> {this.creditsFrom} </span>
            has been <span className="value lowercase"> {this.tradeStatus}</span>,
            effective on <span className="value"> {this.tradeEffectiveDate}</span>.
          </div>
        );
      case CREDIT_TRANSFER_TYPES.part3Award.id:
        return (
          <div className="text-representation">
            An <span className="value">award</span> of
            <span className="value"> {this.numberOfCredits} </span>
            credit{(this.numberOfCredits > 1) && 's'} earned by
            <span className="value"> {this.creditsTo} </span> for the completion of a
            Part 3 Agreement has been <span className="value lowercase"> {this.tradeStatus}</span>,
            effective on <span className="value"> {this.tradeEffectiveDate}</span>.
          </div>
        );
      default:
        return (
          <div className="text-representation">
            A credit transfer of
            <span className="value"> {this.numberOfCredits} </span> credit{(this.numberOfCredits > 1) && 's'} for
            <span className="value"> {this.creditsTo} </span>
            has been <span className="value lowercase"> {this.tradeStatus} </span>
            effective on <span className="value"> {this.tradeEffectiveDate}</span>.
          </div>
        );
    }
  }
}

CreditTransferTextRepresentation.defaultProps = {
  creditsFrom: {
    name: 'From'
  },
  creditsTo: {
    name: 'To'
  },
  tradeEffectiveDate: ''
};

CreditTransferTextRepresentation.propTypes = {
  creditsFrom: PropTypes.shape({
    name: PropTypes.string,
    id: PropTypes.number
  }),
  creditsTo: PropTypes.shape({
    name: PropTypes.string,
    id: PropTypes.number
  }),
  fairMarketValuePerCredit: PropTypes.oneOfType([
    PropTypes.string,
    PropTypes.number
  ]).isRequired,
  numberOfCredits: PropTypes.oneOfType([
    PropTypes.string,
    PropTypes.number
  ]).isRequired,
  status: PropTypes.shape({
    id: PropTypes.number,
    status: PropTypes.string
  }).isRequired,
  tradeEffectiveDate: PropTypes.string,
  tradeType: PropTypes.shape({
    id: PropTypes.number,
    name: PropTypes.string,
    theType: PropTypes.string
  }).isRequired,
  totalValue: PropTypes.oneOfType([
    PropTypes.string,
    PropTypes.number
  ]).isRequired
};

export default CreditTransferTextRepresentation;