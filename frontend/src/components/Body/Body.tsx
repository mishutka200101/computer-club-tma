import styles from "./Body.module.css";

import { Switch } from "../Switch/Switch";
import { PCCard } from "../PCCard/PCCard";
import { PSCard } from "../PSCard/PSCard";

import { useState } from "react";

export interface IButtonsClicked {
  [key: string]: boolean;
}

export function Body() {
  const [buttonsClicked, setButtonsClicked] = useState<IButtonsClicked>({
    PC: true,
    PS: false,
  });
  const currentButtonClicked = Object.keys(buttonsClicked).find(
    (key) => buttonsClicked[key] === true
  );

  return (
    <>
      <div className={styles.body}>
        <Switch
          buttonsClicked={buttonsClicked}
          setButtonsClicked={setButtonsClicked}
        />
        {currentButtonClicked === "PC" ? <PCCard /> : <PSCard />}
      </div>
    </>
  );
}
