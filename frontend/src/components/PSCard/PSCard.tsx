import styles from "./PSCard.module.css";

import { PSCardButton } from "../Buttons/PSCardButton";
import { useState } from "react";

export type TButtonClicked = "1" | "2" | "3" | undefined;

export function PSCard() {
  const [buttonClicked, setButtonClicked] = useState<TButtonClicked>(undefined);

  const resetButton = () => {
    setButtonClicked(undefined);
  };

  return (
    <div className={styles.PSCard}>
      <div className={styles.buttonsHolder} onClick={resetButton}>
        <PSCardButton
          text="1"
          buttonClicked={buttonClicked}
          setButtonClicked={setButtonClicked}
        />
        <PSCardButton
          text="2"
          buttonClicked={buttonClicked}
          setButtonClicked={setButtonClicked}
        />
        <PSCardButton
          text="3"
          buttonClicked={buttonClicked}
          setButtonClicked={setButtonClicked}
        />
      </div>
    </div>
  );
}
