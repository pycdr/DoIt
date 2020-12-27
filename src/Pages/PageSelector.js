import React from "react";
/*import Year from "./YearPage.js";
import Month from "./MonthPage.js";
import Day from "./YearPage.js";
import Time from "./TimePage.js";*/
import { Collapse, Card, Modal, Space, Image, Button } from "antd";
import "antd/dist/antd.css";
import { EyeOutlined } from "@ant-design/icons";
const { Panel } = Collapse;

class PageSelector extends React.Component {
	constructor(props){
		super(props);
		this.data = props.data;
		this.state = {
			y_visibility : {},
			m_visibility : {},
			d_visibility : {},
			t_visibility : {}
		}
	}
	render(){
		if ("data" in this.data){
			return <PageSelector data={this.data["data"]} />
		} else {
			let years, months, days, times;
			
			if (this.data.year === undefined) years = [];
			else if (!Array.isArray(this.data.year)) years = Array(this.data.year);
			else years = this.data.year;
			
			if (this.data.month === undefined) months = [];
			else if (!Array.isArray(this.data.month)) months = Array(this.data.month);
			else months = this.data.month;
			
			if (this.data.day === undefined) days = [];
			else if (!Array.isArray(this.data.day)) days = Array(this.data.day);
			else days = this.data.day;
			
			if (this.data.time === undefined) times = [];
			else if (!Array.isArray(this.data.time)) years = Array(this.data.time);
			else times = this.data.time;
			
			return (
				<Collapse accordion defaultActiveKey={["y","m","d","t"].find(x=>{
					return {"y": years, "m": months, "d": days, "t": times}[x].length!==0
				})}>
					{Object.keys(years).length === 0?<></>:
					<Panel header="Years" key="y"><Space wrap>
						{years.map(x => (
						<Card
							title={x["@number"]}
							extra={
							<Button
								icon={<EyeOutlined />}
								onClick={()=>{
									this.state.y_visibility[x["@number"]] = true;
									this.setState(this.state);
								}}
								>
								show
							</Button>
							}
						>
							<Modal
								title={"detail for year "+x["@number"]}
								visible={this.state.y_visibility[x["@number"]]}
								width="90vw"
								onOk={()=>{
									this.state.y_visibility[x["@number"]] = false;
									this.setState(this.state);
								}}
								onCancel={()=>{
									this.state.y_visibility[x["@number"]] = false;
									this.setState(this.state);
								}}
							>
							{Object.keys(x).map(y => {
								if (y[0]!=="@") return <PageSelector data={{month:x[y]}} />
							})}
							</Modal>
							<Image src={x["@image"]} height="15vw"/>
						</Card>
						))}
					</Space></Panel>
					}
					
					
					{Object.keys(months).length === 0?<></>:
					<Panel header="Months" key="m"><Space wrap>
						{months.map(x => (
						<Card
							title={x["@number"]}
							extra={
							<Button
								icon={<EyeOutlined />}
								onClick={()=>{
									this.state.m_visibility[x["@number"]] = true;
									this.setState(this.state);
								}}
								>
								show
							</Button>
							}
						>
							<Modal
								title={"detail for month "+x["@number"]}
								visible={this.state.m_visibility[x["@number"]]}
								width="80vw"
								onOk={()=>{
									this.state.m_visibility[x["@number"]] = false;
									this.setState(this.state);
								}}
								onCancel={()=>{
									this.state.m_visibility[x["@number"]] = false;
									this.setState(this.state);
								}}
							>
							{Object.keys(x).map(y => {
								if (y[0]!=="@") return <PageSelector data={{day:x[y]}} />
							})}
							</Modal>
							<Image src={x["@image"]} height="15vw"/>
						</Card>
						))}
					</Space></Panel>
					}
					
					
					{Object.keys(days).length === 0?<></>:
					<Panel header="Days" key="d"><Space wrap>
						{days.map(x => (
						<Card
							title={x["@number"]}
							extra={
							<Button
								icon={<EyeOutlined />}
								onClick={()=>{
									this.state.d_visibility[x["@number"]] = true;
									this.setState(this.state);
								}}
								>
								show
							</Button>
							}
						>
							<Modal
								title={"detail for day "+x["@number"]}
								visible={this.state.d_visibility[x["@number"]]}
								width="70vw"
								onOk={()=>{
									this.state.d_visibility[x["@number"]] = false;
									this.setState(this.state);
								}}
								onCancel={()=>{
									this.state.d_visibility[x["@number"]] = false;
									this.setState(this.state);
								}}
							>
							{JSON.stringify(x)} //temporary
							</Modal>
							<Image src={x["@image"]} height="15vw"/>
						</Card>
						))}
					</Space></Panel>
					}
					
					
					{Object.keys(times).length === 0?<></>:
					<Panel header="Times" key="t">
					
					</Panel>
					}
				</Collapse>
			)
		}
	}
}

export default PageSelector;
