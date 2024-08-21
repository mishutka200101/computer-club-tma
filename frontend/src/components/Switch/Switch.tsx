import styles from "./Switch.module.css";

import { SwitchButton } from "../Buttons/SwitchButton";
import { IButtonsClicked } from "../Body/Body";

export function Switch({
  buttonsClicked,
  setButtonsClicked,
}: {
  buttonsClicked: IButtonsClicked;
  setButtonsClicked: (arg0: IButtonsClicked) => void;
}) {
  return (
    <div className={styles.switch}>
      <SwitchButton
        type="PC"
        buttonsClicked={buttonsClicked}
        setButtonsClicked={setButtonsClicked}
      />
      <div className={styles.divider}></div>
      <SwitchButton
        type="PS"
        buttonsClicked={buttonsClicked}
        setButtonsClicked={setButtonsClicked}
      />
    </div>
  );
}
