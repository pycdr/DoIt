import React, {useState} from "react";
import { Space, Skeleton, Button, Table, Modal } from "antd";
import PageSelector from "./PageSelector.js";
import ShowTimes from "./TimePage.js";

class SButton extends React.Component {
	constructor(props){
		super(props);
		this.data = props.data;
		this.state = {show: false};
	}
	render(){
		return (<>
			<Button
				type="dashed"
				style={{borderColor: "#1890ff"}}
				onClick={()=>{this.setState({show:true})}}
			>
				{this.data["@number"]}
			</Button>
			<Modal
				title={"details for day "+this.data["@number"]}
				visible={this.state.show}
				width="70vw"
				onOk={()=>{
					this.setState({show: false});
				}}
				onCancel={()=>{
					this.setState({show: false});
				}}
			>
				<ShowTimes data={this.data["time"]} />
			</Modal>
		</>);
	}
}
function data_render(data){
	if (data===undefined) return <></>;
	else if (data.time===undefined) return (
		<Button
			type="text"
		>
			{data["@number"]}
		</Button>
	);
	return <SButton data={data} />;
}

class Calendar extends React.Component {
	constructor(props){
		super(props);
		this.month_data = props.mdata;
		this.state = {};
		this.table_cols = [
			{title: "Sat", dataIndex: "sat", key: "sat", render: data_render},
			{title: "Son", dataIndex: "son", key: "son", render: data_render},
			{title: "Mon", dataIndex: "mon", key: "mon", render: data_render},
			{title: "Tue", dataIndex: "tue", key: "tue", render: data_render},
			{title: "Wed", dataIndex: "wed", key: "wed", render: data_render},
			{title: "Thu", dataIndex: "thu", key: "thu", render: data_render},
			{title: "Fri", dataIndex: "fri", key: "fri", render: data_render}
		];
		let days;
		if (this.month_data.day === undefined) days = [];
		else if (!Array.isArray(this.month_data.day)) days = Array(this.month_data.day);
		else days = this.month_data.day;
		this.table_data = [];
		//let sat=[], son=[], mon=[], tue=[], wed=[], thu=[], fri=[];
		let _temp_obj = {};
		const week_names = ["sat", "son", "mon", "tue", "wed", "thu", "fri"]
		let fwn = Number(this.month_data["@weekfrom"]);
		for (let i = 1; i <= fwn; ++i){
			_temp_obj[week_names[(i-1)%7]] = undefined;
		}
		let days_obj = {};
		days.map(x => {
			days_obj[Number(x["@number"])] = x;
		});
		for (let i = 1; i <= Number(this.month_data["@count"]); i++){
			if (days_obj[i] === undefined) days_obj[i] = {
				"@number": String(i)
			}
			_temp_obj[week_names[(i+fwn-1)%7]] = days_obj[i];
			if (Object.keys(_temp_obj).length==7){
				this.table_data.push(_temp_obj);
				_temp_obj = {};
			}
		}
		if (Object.keys(_temp_obj).length!==0) this.table_data.push(_temp_obj);
	}
	render(){
		return (
			<Space wrap>
				<Table
					columns={this.table_cols}
					dataSource={this.table_data}
					style={{width:"75vw"}} />
			</Space>
		);
	}
}
export default Calendar;
